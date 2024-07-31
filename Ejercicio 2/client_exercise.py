import sys
import grpc
import exercise_pb2
import exercise_pb2_grpc

if len(sys.argv) != 3:
    print("usage: ./client_exercise.py <host> <port>")
    sys.exit(1)

server = sys.argv[1]
port = sys.argv[2]
channel = grpc.insecure_channel(f'{server}:{port}')
stub = exercise_pb2_grpc.IdentifyStub(channel)

message = exercise_pb2.ID(dni = '123456789q', email='a.b@alu.uclm.es', fullname='A B C')
stub.sendID(message)
