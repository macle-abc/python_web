import axios from 'axios';

function GetProductsInfos() {
    return axios.get("https://api.akmduj.cn/products/")
}

function GetCategories(){
    // products/categories/
    return axios.get("https://api.akmduj.cn/products/categories/")
}

function GetProductsByCategories(url) {
    return axios.get(url)
}

function GetProductDetail(url) {
    return axios.get(url)
}

export {
    GetProductsInfos,
    GetCategories,
    GetProductsByCategories,
    GetProductDetail,
}
