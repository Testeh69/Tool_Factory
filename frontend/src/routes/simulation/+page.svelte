<script lang="ts">
import ElmObs from "./observeur/ElmObs.svelte";
import ElmActToggle from "./actionneur/ElmActToggle.svelte";
import ElmActInput from "./actionneur/ElmActInput.svelte";

interface urlObject {
  urlWebSocket:string;
  urlApi:string;
}

const urlObject: urlObject = {
  urlWebSocket: "ws://127.0.0.1:8081",
  urlApi:"http://127.0.0.1:8081"
}





interface Actionneur{
    listNameAct: string[],
    listNameEndPoint: string[],
    listNameJson: string[]  
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

interface Observateur {
    listNameObs: string[],
    listNameEndPoint: string[],
    listNameJson: string[]       
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

// <uniquifier>: Use a unique and descriptive class name
// <weight>: Use a value from 100 to 900

.section__virtualisation{
    color: #f7f7f7;
    font-family: "Montserrat", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
    display: flex;
    flex-direction: row;
    background-color: #D9AFD9;
    background-image: linear-gradient(0deg, #807eff 0%, #97D9E1 100%);
    justify-content: space-evenly;
    align-items: center;
    height:100vh;
    .observeur__section{
        width:30vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background:linear-gradient(to bottom left,#222328,#a2a8ba);
        height:70vh;
        border-radius: 15px;
        border: solid 1px black;
        box-shadow: 3px 2px 2px black;
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
            border: solid;
            border-radius: 10px;
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
        background:linear-gradient(to bottom left,#222328,#a2a8ba);
        height:70vh;
        border-radius: 15px;
        border: solid 1px black;
        box-shadow: 3px 2px 2px black;
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


</style>
<section class="section__virtualisation">
    <section class="observeur__section">
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
    <section class="actionneur__section">
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
</section>


