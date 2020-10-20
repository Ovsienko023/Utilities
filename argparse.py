import argparse

print("Тело программы")

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--val', help='value in storage.data')
    parser.add_argument('-k', '--key', help='key in storage.data')
    parser.add_argument('-c', '--cope', help='qwerty cope')
    args = parser.parse_args()
    
    return {
        "key": args.key,
        "val": args.val,
        "cope": args.cope
    }



def main():
    
    args = create_parser()
    if args.get("key"):
        print(args["key"])
    

main()