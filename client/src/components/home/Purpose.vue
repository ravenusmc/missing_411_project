<template>
<div>
	<h3 class='title center'>The Purpose</h3>
	<div class='paragraph-div'>
		<p>Ok, sometime during Covid or shortly after Covid I watched a documentary on Amazon. 
			the documentary was about people who went missing in national parks. More than that though
			it argued that there was something more going on. As I watched the documentary I wondered
			if I could get some of the data and examine it myself. I love doing data projects and it 
			seemed perfect. Well a lot of time went by, I got busy with work, other projects etc and 
			I never spent that much time trying to track down data.  
		</p>
		<p>
			In the last few months I really started to look for some data on missing 411 and managed 
			to find something on Kaggle. The problem was that the data was very small. I was disappointed 
			by this. I wanted more data - not a data set that has around 60 samples in it. To me, 
			that's almost a joke. Yet, I decided to push on with the project and instead of using 
			Google Charts, I'd use D3.JS to make the charts. 
		</p>
	</div>
</div>
</template>

<script>
export default {
  name: "Purpose",
};
</script>

<style scoped>

.title {
	font-size: 2.5rem;
	text-transform: uppercase;
}

.paragraph-div {
	margin: 100px;
	display: grid;
	grid-template-columns: 1fr 1fr;
	border: 2px solid red;
	font-size: 1.5rem;
}

</style>