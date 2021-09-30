var Links = {
    setColor:function(color){
      var alist = document.querySelectAll('a');
      var i = 0;
      while(i < alist.lenth){
        alist[i].style.color = color;
        i = i + 1;
      }
    }
  }
  var Body = {
    setColor:function (color){
      document.querySelector('body').style.color = color;
    },
    setBackgroundColor:function(color){
      document.querySelector('body').style.backgroundColor = color;
    }
  }

  