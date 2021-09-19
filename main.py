import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.153',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


def get_data_file(headers):
    """ Collect data and return JSON file"""
    # url = 'https://www.landingfolio.com/'
    # req = requests.get(url=url, headers=headers)
    #
    # with open('index.html', 'w') as file:
    #     file.write(req.text)

    result_list = []
    img_count = 0
    offset = 0
    while True:
        url = f'https://s1.landingfolio.com/api/v1/inspiration/?offset={offset}&color=%23undefined'

        response = requests.get(url=url, headers=headers)
        data = response.json()

        for item in data:
            if 'description' in item:
                images = item.get('images')
                for img in images:
                    img.update({'url': f'https://landingfoliocom.imgix.net/{img.get("url")}'})
                img_count += len(images)
                result_list.append(
                    {
                        'title': item.get('title'),
                        'description': item.get('description'),
                        'url': item.get('url'),
                        'images': images
                    }
                )
            else:
                with open('result_list.json', 'a') as file:
                    json.dump(result_list, file, indent=4, ensure_ascii=False)

                return f'[INFO] Work finished. Images count is: {img_count}\n{"=" * 20 }'

        print(f'[+] Processed {offset}')
        offset += 1


def download_imgs(file_path):
    """ Download images """
    pass


def main():
    get_data_file(headers=headers)


if __name__ == '__main__':
    main()
