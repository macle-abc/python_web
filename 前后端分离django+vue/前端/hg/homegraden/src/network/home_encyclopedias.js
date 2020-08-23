import axios from 'axios'

function GetHomeEncyclopedias() {
    return axios.get("https://api.akmduj.cn/home_encyclopedias/")
}

export {
    GetHomeEncyclopedias
}