# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import grpc
import math
import random
import helloworld_pb2
import helloworld_pb2_grpc
from datetime import date, timedelta


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self):
        # El centro de la diana sera random entre 50m y 150m
        #self.centro_diana = random.uniform(50, 150)
        self.centro_diana = 120.02
        # para guardar el mejor Disparo
        self.mejor_disparo = None
        # parra guardar el user del mejor disparo
        self.mejor_usuario = None

    def DimeCentroDiana(self, request, context):
        return helloworld_pb2.CentroDianaResponse(speed=self.centro_diana)

    def DisparaCannon(self, request, context):
        try:
            if not (0 <= request.angle <= math.pi / 2):
                context.set_details('The angle must be between 0 y π/2.')
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                return helloworld_pb2.DisparoResponse()

            #Calculo de la speed
            speed_bala = (request.speed ** 2) * math.sin(2 * request.angle) / 9.81
            difference = self.centro_diana - speed_bala

            # Actualizamos el mejor disparo si corresponde
            if self.mejor_disparo is None or abs(difference) < abs(self.mejor_disparo):
                self.mejor_disparo = difference
                self.mejor_usuario = request.username

            return helloworld_pb2.DisparoResponse(difference=difference)
        except Exception as e:
            context.set_details(f'Error processing the shot: {e}')
            context.set_code(grpc.StatusCode.INTERNAL)
            return helloworld_pb2.DisparoResponse()

    def MejorDisparo(self, request, context):
        if self.mejor_usuario is None:
            context.set_details('No shots have been fired yet.')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return helloworld_pb2.MejorDisparoResponse()
        return helloworld_pb2.MejorDisparoResponse(
            username=self.mejor_usuario,
            speed=self.mejor_disparo)

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message=f"Hello again, {request.name}!")

    def NextDate(self, request, context):
        try:
            # log
            logging.info(f"Received NextDate request with: year={request.year}, month={request.month}, day={request.day}")
            # Creamos un objeto date con los datos del request
            currentDate = date(request.year, request.month, request.day)
            # aumentamos un dia
            nextDay = currentDate + timedelta(days=1)
            logging.info(f"Computed next date: {nextDay}")
            # lo retornamos
            return helloworld_pb2.ReplyDate(
                day=nextDay.day,
                month=nextDay.month,
                year=nextDay.year
            )
        # lanzar excepcion si hay error
        except ValueError as e:
            logging.error(f"Error  NextDate: {e}")
            context.set_details(f'Error en la fecha: {e}')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return helloworld_pb2.ReplyDate()
    def AddDaysDate(self, request, context):
        try:
            # log
            logging.info(f"Received AddDaysDate request: year={request.year}, month={request.month}, day={request.day}, daysToDate={request.dayToAdd}")
            currentDate = date(request.year, request.month, request.day)
            dateResul = currentDate + timedelta(days=request.dayToAdd)
            logging.info(f"Computed date after adding days: {dateResul}")
            
            # Retornar la fecha resultante
            return helloworld_pb2.ReplyDate(
                day=dateResul.day,
                month=dateResul.month,
                year=dateResul.year
            )
        except ValueError as e:
            logging.error(f"Error processing AddDaysDate: {e}")
            context.set_details(f'Error en la fecha: {e}')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return helloworld_pb2.ReplyDate()

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)   
    server.add_insecure_port("[::]:" + port)
    server.start()
    logging.info("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    serve()
