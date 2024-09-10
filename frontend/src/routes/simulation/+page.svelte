<script lang="ts">
import ElmObs from "./observeur/ElmObs.svelte";
import ElmActToggle from "./actionneur/ElmActToggle.svelte";
import ElmActInput from "./actionneur/ElmActInput.svelte";
import {fly} from "svelte/transition"
import type { urlObject, Actionneur, Observateur } from './types'; 
import Safran from "../../assets/Logo_Safran.svg"


const urlObject: urlObject = {
  urlWebSocket: "ws://127.0.0.1:8081",
  urlApi:"http://127.0.0.1:8081"
}



const objActionneurInput: Actionneur = {
    listNameAct:[
        "Sélectionner l'étape du programme",
        "Sélectionner le nombre de pièce chargé",
        "Sélectionner le temps de cycle de la machine"
    ],
    listNameEndPoint:[
        "/historique",
        "/parts",
        "/cycle"
    ],
    listNameJson:[
        "step_program",
        "number_parts",
        "time_cycle"
    ]
}

const objActionneurToggle: Actionneur = {
    listNameAct:[
                "Charger/Supprimer un plan",
                "Fermer/Ouvrir la porte",
                "Allumer/Eteindre la gravure"],
    listNameEndPoint:[
                "/scan",
                "/porte",
                "/statemachine"],
    listNameJson:[
            "state_scan",
            "porte_ouverte",
            "state_machine"
    ]
}



const objObservateur: Observateur = {
    listNameObs:["Programme",
                "Porte",
                "Machine",
                "Numéro de l'étape",
                "Nombre de pièces",
                "Temps de cycle"
                ],
    listNameEndPoint:["/scan",
                "/porte",
                "/statemachine",
                "/historique",
                "/parts",
                "/cycle"
    ],
    listNameJson: ["scan_status",
                "Porte_Ouverte",
                "state_machine",
                "historique",
                "number_parts",
                "time_cycle"
    ]

}

</script>
<style lang="scss">


.section__virtualisation{
    background-color: #0f0c29;
    background: linear-gradient(#0f0c29,#302b63,#24243e);
    color: #f7f7f7;
    font-family:sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    height:100vh;
    .observeur__section{
        width:30vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: hsla(0%,0%,23%,1);
        height:70vh;
        border-radius: 5px;
        
        .title{
            font-weight: bold;
        }
        .observeur{
            display: grid;
            grid-template-columns: auto auto ;
            font-size: 12px;
            width: 93%;
            height:90%;
            align-items: center;
            align-items: center;
            justify-content: space-evenly;
        }
    }
    .actionneur__section{
        width:40vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: hsla(0%,0%,23%,1);
        height:70vh;
        border-radius: 5px;
     
        .title{
            font-weight: bold;
        }
        .actionneur{
            display: grid;
            grid-template-columns: auto auto;
            width: 90%;
            height:90%;
            align-items: center;
            border-radius: 10px;
            align-items: center;
            justify-content: space-evenly;
        }
    }
}
.safran{
  position: absolute;
  top:30%;
  left: 10%;
  z-index: -1;
}

@media (max-width: 700px){
    
} 

</style>
<section class="section__virtualisation" >
    <section class="observeur__section" transition:fly = {{y:200, duration:1000}}>
        <span class="title">OBSERVEUR</span>
        <div class="observeur">
            {#each objObservateur.listNameObs as obs, index}
                <ElmObs 
                    name = {obs} 
                    endpoint = {objObservateur.listNameEndPoint[index]} 
                    json = {objObservateur.listNameJson[index]} 
                    urlWebSocket = {urlObject.urlWebSocket}
                />
            {/each}
        </div>
    </section>
    <section class="actionneur__section" transition:fly = {{y:200, duration:1000}}>
        <span class="title">ACTIONNEUR</span>
        <div class="actionneur">
            <div class="actionneur__toggle">
                {#each objActionneurToggle.listNameAct as act, index}
                    <ElmActToggle
                    name = {act}
                    endpoint = {objActionneurToggle.listNameEndPoint[index]}
                    json = {objActionneurToggle.listNameJson[index]}
                    jsonObs = {objObservateur.listNameJson[index]}
                    urlApi = {urlObject.urlApi}
                    />
                {/each}
            </div>
            <div class="actionneur__input">
                {#each objActionneurInput.listNameAct as act,index}
                    <ElmActInput
                        name = {act}
                        endpoint = {objActionneurInput.listNameEndPoint[index]}
                        json = {objActionneurInput.listNameJson[index]}
                        urlApi = {urlObject.urlApi}
                    />
                {/each}
            </div>
        </div>
    </section>
    <img src={Safran} alt={Safran} class="safran" />
</section>

