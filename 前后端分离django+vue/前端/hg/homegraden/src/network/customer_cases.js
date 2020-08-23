import axios from 'axios';

function GetCustomerCases() {
    return axios.get("https://api.akmduj.cn/customer_cases/")
}

function GetCustomerCasesImagesDetail(url) {
    return axios.get(url)
}

function GetVideo(url) {
    return axios.get(url)
}

export {
    GetCustomerCases,
    GetCustomerCasesImagesDetail,
    GetVideo,
}