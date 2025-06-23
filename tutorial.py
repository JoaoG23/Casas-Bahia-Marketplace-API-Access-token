import requests
import json

def get_products():
    url = "https://api-mktplace-hlg.viavarejo.com.br/api/v4/sandbox/api-front-products-v4/jersey/product"
    headers = {
        'client_id': '2112asasda',
        'access_token': '20202022',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    params = {
        'pagina': 1,
        'itensPorPagina': 20
    }
    
    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )
    
    return response.json()

if __name__ == "__main__":
    result = get_products()
    print(json.dumps(result, indent=2, ensure_ascii=False))
