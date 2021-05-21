$(document).ready(function(){
	$(".item-two-columns img, .item-three-columns img, .item-four-columns img, .profile-pic img").hover(function(){
		$(this).fadeTo(150, 0.06);
	},function(){
   		$(this).fadeTo(150, 1.0);
	});
});