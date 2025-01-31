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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
from datetime import date, timedelta
import grpc
import math
import random
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        try : 

            stub = helloworld_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
            
            print("Greeter client received: " + response.message)
            # Exercise 1
            print("Exercise 1")
            # fecha actual
            dateNow  =date.today()
            day=12
            month=12
            year=2024
            #response = stub.NextDate(helloworld_pb2.RequestDate(day=dateNow.day, month=dateNow.month, year=dateNow.year))
            response = stub.NextDate(helloworld_pb2.RequestDate(day = day,month=  month,year = year))
            print(f"Current date: {year}-{month}-{day}\n")
            print(f"Next date: {response.year}-{response.month}-{response.day}\n")

            #Exercise 2
            print("Exercise 2")
            ## add days
            daysToAdd = 10
            response = stub.AddDaysDate(
            helloworld_pb2.RequestAddDay(
                day=dateNow.day,
                month=dateNow.month,
                year=dateNow.year,
                dayToAdd=daysToAdd)
            )
            print(f"Date before adding {daysToAdd} days: {dateNow.year}-{dateNow.month}-{dateNow.day}\n")
            print(f"Date after adding {daysToAdd} days: {response.year}-{response.month}-{response.day}\n")

            # Exercise 3
            print("Exercise 3")
            #Obtenemos el centro de la diana
            centro_response = stub.DimeCentroDiana(helloworld_pb2.Empty())
            print(f"Target center a {centro_response.speed} meters.")

            #Disparamos hasta acertar al centro
            acertado = False
            while not acertado:
                angle = float(input("Enter the angle in radian (0-1.57): "))
                speed = float(input("Enter the speed in m/s: "))
                username = input("Enter your name: ")

                disparo_response = stub.DisparaCannon(
                    helloworld_pb2.DisparoRequest(
                        username=username,
                        angle=angle,
                        speed=speed
                    )
                )
                print(f"Difference: {disparo_response.difference} meters.")
                if abs(disparo_response.difference) <= 1:
                    print("You hit the bull's eye!")
                    acertado = True

            # Consultamosel mejor disparo
            mejor_response = stub.MejorDisparo(helloworld_pb2.Empty())
            print(f"The best shot was by {mejor_response.username}, with a difference of {mejor_response.speed} meters.")

        except grpc.RpcError as e:
            print(f"Error : {e.details()})")
            

if __name__ == "__main__":
    logging.basicConfig()
    run()
