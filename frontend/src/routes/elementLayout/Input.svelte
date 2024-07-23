<script lang="ts">
import Launch from "../../assets/launch.svg"
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
        &:focus{
            border: none;
        }
    }
}

.launch__program{
    background-color: transparent;
    width:17%;
    height:90%;
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    border-radius: 5px;
    .Launch{
        height:90%;
        width: 90%;
        filter: brightness(0) invert(1);
    }
    &:hover{
        background-color: white;
    }
    &:hover .Launch{
        filter: none;
    }
}

</style>


<div class="load__program">
    <input type ="search">
</div>
<button class="launch__program">
    <img src={Launch} alt={Launch} class="Launch" />
</button>
