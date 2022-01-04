from database import Database


def main():
    Database.get_instance().posts.insert_one({
        'test': 'ok'
    })


if __name__ == '__main__':
    main()
