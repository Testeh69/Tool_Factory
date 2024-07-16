<script>
    import quarkus from "../assets/quarkus.svg"
    import pictures from "../assets/pictures.svg"
</script>
<style lang="scss">
    .menu{
        position: absolute;
        top:25%;
        height:60vh;
        display: flex;
        flex-direction: column;

        .nav__bar{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-color: red;
            width:50px;
            height: 80%;
          
                img{
                    margin: 20px;
                    width: 30px;
                    height: auto;
                }
            
        }
    }
</style>
<div class="menu">
    <nav class="nav__bar">
        <a href="/simulation"><img src = {quarkus} alt = {quarkus}></a>
        <a href = "/pictures"><img src = {pictures} alt = {pictures}></a>
    </nav>
</div>

<slot/>