from storage.json_storage import load_data, save_data

def main():
    data = load_data()
    save_data(data)

if __name__ == '__main__':
    main()


