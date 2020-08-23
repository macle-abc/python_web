import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    englishTitle: "",
    title: "",
    list: [],
  },
  mutations: {
    ChangeEnglishTitle(state, newEnglishTitle){
      // console.log(newEnglishTitle);
      state.englishTitle = newEnglishTitle;
      // console.log("这是修改英文标题");
    },
    ChangeTitle(state, newTitle){
      state.title = newTitle;
      // console.log(newTitle);
      // console.log("这是修改标题");
    },
    ChangeList(state, newList){
      state.list = newList;
      // console.log(newList);
      // console.log("这是修改list");
    },
    WhoClick(state, which){
      // console.log(which);
      for (const item of state.list)
      {
        if (item === which)
        {
          item.isActive = true;
        }
        else{
          item.isActive = false;
        }
      }
    }
  },
  actions: {
  },
  modules: {
  },
  getters: {
    GetList(state) {
      return state.list;
    }
  }
})
