<script lang="ts">
    import quarkus from "../assets/quarkus.svg"
    import pictures from "../assets/pictures.svg"
    import logo from "../assets/logo.jpeg"
    import menu from "../assets/menu.svg"
    import cross from "../assets/cross.svg"
    import Power from "./elementLayout/Power.svelte"
  import Input from "./elementLayout/Input.svelte";
    
    let manual_state: boolean = false;


    const handleChangeManualState = () => {
        manual_state = manual_state ? false:true;
        console.log(manual_state)    
    }


</script>
<style lang="scss">

    .menu{
        border-bottom: 0.1px #fff solid;
        font-size: 70%;
        position: absolute;
        height:30px;
        width: 100%;
        background:transparent;
        display: flex;
        align-items: center;
        .logo__nav{

            padding: 0;
            margin: 0;
            color:black;
            width:130px;
            height:40px;
            text-decoration: none;
            display: flex;
            .logo{
                color:#fff;
                height:40px;
                display: flex;
                flex-direction: row;
                align-items: center;
        
            h5{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-style: italic;
                font-weight:bold;
                color:white;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: row;
                padding-left: 3px;
            }
            img{
                    height:30px;
                    width:30px;
                    color:white;
                    padding-left:0px;
                    border-radius:3px;
                  
            }
        }
    }
        .nav__bar{
            position: relative;
            left:calc(100% - 43%);
            display: flex;
            justify-content: flex-end;
            height:40px;
            justify-content: space-evenly;
            align-items: center;
            .nav__element{
                color:#fff;
                display: flex;
                flex-direction: row;  
                align-items: center;
                justify-content: space-evenly;
                height: 100%;
                padding-right: 20px;
                transition: background-color 500ms ease;
                &:hover span{
                        font-style: oblique;
                        color:white;
                    }
                &:hover img{
                    filter: brightness(0) invert(1);

                }

                &:hover{
                    background-color: #0f0c29;
                    background: linear-gradient(#0f0c29,#302b63,#24243e);
                    border-bottom-left-radius: 5px;
                    border-bottom-right-radius: 5px;
                    height:70%;
                }
                img{
                    color:white;
                    margin: 20px;
                    width: 20px;
                    height: auto;
                    transition: filter 500ms ease;
                }
                span{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    color:rgb(42, 35, 56);
                    font-size:0.8em;
                    font-style: italic;
                    transition: color 500ms ease;
                    
                }
                a{  
                    color:#fff;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color:black;
                    text-decoration: none;
                }
            }
        }
    }
.menu__ur{
    position: absolute;
    top:94%;
    left:69%;
    width:30%;
    display: flex;
    justify-content: center;
    align-items: center;
    height:5%;
    .ur_manual{
        border: solid 1px white;
        background-color: #0f0c29;
        background: linear-gradient(#0f0c29,#302b63,#24243e);
        border-radius: 7px;
        position: absolute;
        left:90%;
        height:100%;
        display: flex;
        justify-content: center;
        align-items: center;
        img{
            height:90%;
            width: 90%;
            filter: brightness(0) invert(1);
            transition:display 500ms;
        }
    }
    .control_ur{
        position: absolute;
        right:15%;
        border: solid 1px white;
        background-color: #0f0c29;
        background: linear-gradient(#0f0c29,#302b63,#24243e);
        display: flex;
        flex-direction: row;
        width:120%;
        height:120%;
        justify-content: space-evenly;
        align-items: center;
        border-radius: 7px;
        .input__program{
            width:70%;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: space-evenly;
        }
        .power__on{
            width:40%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    }
}

@media (max-width: 879px) {
    .menu{
    .nav__bar{
        position: absolute;
        left:calc(100% - 42%);
    }
}

}

</style>
<div class="menu">
    <a href = "/" class="logo__nav">
        <span class="logo">
            <img src={logo} alt = {logo} id = {logo}>
            <h5>Tool Factory UR</h5>
        </span>
    </a>
    <nav class="nav__bar">
        <div class="nav__element">
            <a href="/simulation">
                <img src = {quarkus} alt = {quarkus}>            
                <span>Simulation Integration</span>
            </a>
        </div>
        <div class="nav__element">
            <a href = "/pictures">
                <img src={pictures} alt={pictures}/>
                <span>Traitement des photos</span>
            </a>
        </div>
    </nav>
</div>

<div class="menu__ur">
    <button class="ur_manual" on:click={handleChangeManualState}>
        <img src={cross} alt={cross} style = {manual_state ? "display:visible": "display:none"} class="svg_cross">
        <img src={menu} alt={menu} style={manual_state ? "display:none": "display:visible"} class="svg_menu">
    </button>
    <div class="control_ur {manual_state ? "open":""}" style = "{manual_state? "display:visible":"display:none"}">
        <span class="power__on">
            <Power />
        </span>
        <span class="input__program">
            <Input/>
        </span>
    </div>
</div>
 

<slot/>