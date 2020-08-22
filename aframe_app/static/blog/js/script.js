$(window).scroll(function(evt){
    if($(window).scrollTop() > 0){
      $(".navbar").removeClass("navbar-top");
      $(".navbar").addClass("bg-light");
      $(".navbar").addClass("navbar-light ");
    }
  else{
    $(".navbar").addClass("navbar-top");
    $(".navbar").removeClass("bg-light");
    $(".navbar").removeClass("navbar-light ");    
  }
});

// 啟用skroller涵式庫需要初始化
var s = skrollr.init();