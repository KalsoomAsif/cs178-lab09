import boto3

TABLE_NAME = "Books"

def get_table():
    dynamodb = boto3.resource("dynamodb", region_name="us-east-2")
    return dynamodb.Table(TABLE_NAME)

def print_all_books():
    table = get_table()

    response = table.scan()
    items = response.get("Items", [])

    print(f"\nFound {len(items)} book(s):\n")

    for book in items:
        print(f"Title : {book.get('Title')}")
        print(f"Author: {book.get('Author')}")
        print(f"Pages : {book.get('Pages')}")
        print()

def main():
    print("==== Reading Books from DynamoDB ====")
    print_all_books()

if __name__ == "__main__":
    main()