<template>
    <div>
        <h2>
            FRUITLIST
        </h2>
        <input type="text" v-model="keyword" @input="getresults" placeholder="SEARCH FRUITS DATA"/>
        <p>Results are :</p>
        <div>
            <center>
            <table border="3px" width="50%" margin="50%">
                <tr>
                <td><em><strong><centre>NAME</centre></strong></em></td>
                <td><em><strong><centre>ALIAS</centre></strong></em></td>
                <td><em><strong><centre>VARITIES</centre></strong></em></td>
                </tr>
                <tr v-for="item in list" v-bind:key="item.name">
                <td>{{item.name}}</td>
                <td>{{item.alias}}</td>
                <td>{{item.varities}}</td>
                </tr>
            </table>
            </center>
        </div>    
    </div>
</template>
<script>
//import Vue from 'vue';
//import VueAxios from 'vue-axios';
import axios from 'axios';
//Vue.use(VueAxios,axios)
export default{
        name:"Users",
        data(){
            return{
                keyword:'',
                list : [],
            }
        },
        watch:{
            keyword:function(val){
                if(val.length > 3){
                    this.getresults();
                }
            }
        },
        methods:
        {
            getresults(){
                axios.get('http://127.0.0.1:8000/fruits/?search='+this.keyword)
                .then(resp=>{
                    this.list=resp.data
                    console.log(resp)
                })}
        },
        created(){
            this.getresults()
        }
    }
</script>
