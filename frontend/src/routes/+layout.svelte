<script>
    import quarkus from "../assets/quarkus.svg"
    import pictures from "../assets/pictures.svg"
    import logo from "../assets/logo.jpeg"
</script>
<style lang="scss">
    .menu{
        border: solid 0.1px;
        font-size: 12px;
        position: absolute;
        height:40px;
        width: 100%;
        background: rgb(0,22,250);
        display: flex;
        align-items: center;
        background: linear-gradient(120deg, rgba(0,22,250,1) 0%, rgb(79, 94, 215) 50%, rgba(6,161,254,1) 75%);            
        .logo{
            width:30%;
            display: flex;
            flex-direction: row;
            align-items: center;
            img{
                padding-left:5px;
                padding-right: 5px;
                height:40px;
                width: 40px;
            }
        }
        .nav__bar{
            position: relative;
            left:25%;
            display: flex;
            justify-content: flex-end;
            height:40px;
            justify-content: space-evenly;
            align-items: center;
            .nav__element{
                display: flex;
                flex-direction: row;  
                align-items: center;
                justify-content: space-evenly;
                height: 100%;
                border: solid 0.1px;
                padding-right: 20px;
                img{
                    margin: 20px;
                    width: 20px;
                    height: auto;
                }
                a{  
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color:black;
                    text-decoration: none;
                }
            }
        }
    }
</style>
<div class="menu">
    <span class="logo">
        <img src={logo} alt = {logo} id = {logo}>
        <h5>Tool Factory UR</h5>
    </span>
    <nav class="nav__bar">
        <div class="nav__element">
            <a href="/simulation">
                <img src = {quarkus} alt = {quarkus}>            
                <span>Simulation Integration</span>
            </a>
        </div>
        <div class="nav__element">
            <a href = "/pictures">
                <img src = {pictures} alt = {pictures}>
                <span>Traitement des photos</span>
            </a>
        </div>
    </nav>
</div>

<slot/>