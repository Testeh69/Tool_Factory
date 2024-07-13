<script>
	import MainGet from "./get/mainGet.svelte";
	import MainPost from "./post/mainPost.svelte";
</script>
<style>


main{
	display: flex;
	flex-direction: row;
	align-items: center;
	margin: 0;
	padding: 0;
	width: 100%;
	height: 100%;
	justify-content: center;
}
</style>
<main>
	
	<MainGet />
	<MainPost />
</main>

