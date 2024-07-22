<script lang="ts">
    import quarkus from "../assets/quarkus.svg"
    import pictures from "../assets/pictures.svg"
    import logo from "../assets/logo.jpeg"


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
    top:95%;
    background-color: red;
    left:75%;
    width:25%;
    display: flex;
    justify-content: center;
    align-items: center;
    height:5%;
    .ur_manual{
        background-color: red;
        border-radius: 5px;

    }}

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
    <button class="ur_manual">
        ok
    </button>
    <div class="control_ur" style = "{manual_state? "display:visible":"display:insivisble"}">
        <h1>LOL</h1>
    </div>
</div>
 

<slot/>