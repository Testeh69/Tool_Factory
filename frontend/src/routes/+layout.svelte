<script lang="ts">
    import quarkus from "../assets/quarkus.svg"
    import pictures from "../assets/pictures.svg"
    import logo from "../assets/logo.jpeg"
    import menu from "../assets/menu.svg"
    import cross from "../assets/cross.svg"
    import Power from "./elementLayout/Power.svelte"
  import Input from "./elementLayout/Input.svelte";
    
    let manual_state: boolean = false;
    let menu_state:boolean = false;

    const handleChangeMenuState = () => {
        menu_state = menu_state ? false: true;
    }

    const handleChangeManualState = () => {
        manual_state = manual_state ? false:true;
    }


</script>
<style lang="scss">


.menu_sub{
    display: none;
}
    .menu{
        border-bottom: 0.1px #fff solid;
        font-size: 70%;
        position: absolute;
        height:29px;
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
            display: flex;
            height:29px;

            .nav__element{
                display: flex;
                justify-content: space-around;
                color:#fff;
                display: flex;
                flex-direction: row;  
                align-items: center;
                justify-content: space-evenly;
                height: 100%;
                padding-right: 20px;
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
                    height:100%;
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
                    height:30px;
                }
            }
            .pictures{
                width: 180px;
                position: absolute;
                right:0;
                transition: background-color 5s ease;
                &:hover{
                    background-color: #0f0c29;
                    background: linear-gradient(#0f0c29,#302b63,#24243e);
                    border-bottom-left-radius: 5px;
                    border-bottom-right-radius: 5px;
                    height:100%;
                }}

            }
            .simulation{
                width: 180px;
                transition: background-color 5s ease;
                position: absolute;
                right:200px;
                &:hover{
                    background-color: #0f0c29;
                    background: linear-gradient(#0f0c29,#302b63,#24243e);
                    border-bottom-left-radius: 5px;
                    border-bottom-right-radius: 5px;
                    height:100%;
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
    height:20px;
    .ur_manual{
        border: solid 1px white;
        background-color: #0f0c29;
        background: linear-gradient(#0f0c29,#302b63,#24243e);
        border-radius: 7px;
        position: absolute;
        right: 6px;
        height:100%;
        height: 30px;
        width: 30px;
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
        right:40px;
        border: solid 1px white;
        background-color: #0f0c29;
        background: linear-gradient(#0f0c29,#302b63,#24243e);
        display: flex;
        flex-direction: row;
        width:230px;
        height:30px;
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


@media (max-width: 500px) {
    .menu{
    .nav__bar{
        display: none;
    }
}
.menu_sub{
    display:flex;
    position: absolute;
    right:0%;
    top:0%;
    width:30px;
    height:30px;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    button{
        img{
            height:20px;
            width: 20px;
        }
    }
    .list_menu{
        border: solid 1px white;
        border-radius: 5px;
        border: solid 1px white;
                border-radius: 5px;
            background-color: #fff;
       
        display: flex;
        flex-direction: column;
        width: 200px;
        position: absolute;
        top:30px;
        right:0%;
        height:60px;
        font-size: 12px;
        justify-content: center;
        align-items: center;
        .nav__responsive{
            padding-bottom: 3px;
            &:hover{
                border: solid 1px white;
                border-radius: 5px;
                background-color: #0f0c29;
                background: linear-gradient(#0f0c29,#302b63,#24243e);
            }

            &:hover img{
                filter: brightness(0) invert(1);

            }
            &:hover span{
                color:#fff;
            }
            a{  border-radius: 5px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100%;
                img{

                    height:25px;
                    width: 25px;
                }
                span{
                    padding-left: 4px;
                    color: black;
                    text-decoration:none;
                    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
                    font-style: normal;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 12px;
                }
            }
        }
        .pictures_res{
            width: 100%;
            height:50%;
     
        }
        .simulation_res{
            width: 100%;
            height:50%;
        }
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
        <div class="nav__element simulation">
            <a href="/simulation">
                <img src = {quarkus} alt = {quarkus}>            
                <span>Simulation Integration</span>
            </a>
        </div>
        <div class="nav__element pictures">
            <a href = "/pictures">
                <img src={pictures} alt={pictures}/>
                <span>Traitement des photos</span>
            </a>
        </div>
    </nav>
</div>
<nav class="menu_sub">
    <button class="menu_responsive" on:click={handleChangeMenuState}>
        <img src={cross} alt={cross} style = {menu_state ? "display:visible": "display:none"} class="svg_cross">
        <img src={menu} alt={menu} style={menu_state ? "display:none": "display:visible"} class="svg_menu">
    </button>
    {#if menu_state}
    <div class="list_menu">
        <div class="nav__responsive simulation_res">
            <a href="/simulation">
                <img src = {quarkus} alt = {quarkus}>            
                <span>Simulation Integration</span>
            </a>
        </div>
        <div class="nav__responsive pictures_res">
            <a href = "/pictures">
                <img src={pictures} alt={pictures}/>
                <span>Traitement des photos</span>
            </a>
        </div>
    </div>
    {/if}
</nav>
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