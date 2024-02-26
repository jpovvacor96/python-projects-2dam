from odoo import http
from odoo.http import request
import requests

class ApiController(http.ApiController):

    @http.route('api-products/api_data', type='json', auth='public')
    def get_api_data(self):
        try:
            url='http://localhost:8081/products'
            response=requests.get(url)
            if response.status_code==200:
                api_data=response.json()
                return request.render('api-products.api_data_view', {'data': api_data})
            else:
                response.raise_for_status()
        except Exception as e:
            return {'error': str(e)}