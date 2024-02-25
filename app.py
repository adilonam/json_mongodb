







from mongodb import MongoDb


def main():
    print("Connection string fro Mongodb :" , end = " ")
    uri = input()
    mongodb = MongoDb(uri)
    mongodb.start()


    


if __name__ == '__main__':
    main()
    