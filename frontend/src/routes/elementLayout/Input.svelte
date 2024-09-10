<script lang="ts">
import Launch from "../../assets/launch.svg"



const urlApi :string = "http://127.0.0.1:8081"
const endpoint: string = "/command"
const json: string = "command"

let validated:boolean = true;
let command:String = "";

async function postData(urlApi:string,endpoint:string, json:string){
        try{
            console.log("ok")
            const response = await fetch(`${urlApi}${endpoint}`, 
                {
                    method: "POST",
                    headers:{
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({[json]:command})
                }
            )
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            validated = true;
        } catch (error) {
            console.error("Error sending POST request:", error);
            validated = false;
        }
    }

const sendCommandUr = () => {
    const element = document.querySelector(".search") as HTMLInputElement;
    command = element.value;
    postData(urlApi,endpoint, json)
    element.value = "" ;
}


</script>
<style lang="scss">

.load__program{
    input[type="search"]{
        background-color: hsla(0%,0%,23%,1);
        border: none;
        border-radius: 5px;
        display: flex;
        text-align: center;
        align-items: center;
        color:#fff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 12px;
        width: 110px;
        margin-left: 4px;
        &:focus{
            border: none;
        }
    }
}

.launch__program{
    background: transparent;
    height:29px;
    width: 29px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 5px;
    margin-left: 5px;
    margin-right: 10px;
    border: none;
    .Launch{
        height:26px;
        width: 26px;
        filter: brightness(0) invert(1);
    }
    &:hover{
        background-color: white;
    }
    &:hover .Launch{
        filter: none;
    }
}
@media(max-width:800px){
    .load__program{
        position: absolute;
        right:39%;
        width:25%;
        padding-right: 5px;
        
    }
    .launch__program{
        position: absolute;
        right:-2%;
    }
    
}

@media(max-width:740px){
    .load__program{
        width:80px;
        padding-right: 5px;
        
    }
    .launch__program{
        padding-right: 8px;
        margin-right: 8px;
        height:29px;
        width: 30px;
        img{
            height:29px;
            width: auto;
        }
    }
    
}
</style>


<div class="load__program">
    <input type ="search" class="search">
</div>
<button class="launch__program" on:click = {sendCommandUr}>
    <img src={Launch} alt={Launch} class="Launch" />
</button>
