import axios from 'axios';

function GetConsultingNews(){
    return axios.get("https://api.akmduj.cn/consulting_news/")
}



export {
    GetConsultingNews
}