/*重置样式*/
/*
html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr,
acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub
, sup, tt, var, b, u, i, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody,
tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header,
hgroup, menu, nav, output, section, summary, time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    position: static;
}
*/
/*重置样式*/

* {
    margin: 0;
    padding: 0;
    border: 0;
    position: static;
    }

.box-shadow-card {
    box-shadow: 0 7px 10px -5px rgba(255,152,0,.4);
    box-shadow: 2px 2px 5px #000;
}

body {
  /*
  margin-left:20% ;
  margin-right: 20%;
  */
  text-align: center;
  /*
  background-color: balck;
  */
}

.sign_in_table{
  /*
  background-color: gray;
  */
  height: 647px;
}

/*header*/
.header-line {
    width: 100%;
    height: 100px;
    background-image: url("./resources/snipaste_20180415_1454011.png");
    background-size:100% 100px;
}

.bottom {
  width: 100%;
  height: 50px;
  position: relative;
  bottom: 0;
  background: #970c14;
  text-align:right;

}

.log_in_info{
  background: #f6f610db repeat;
}

.login_area{
  width: 300px;
  height: 310px;
  margin: 20px auto;
  display: block;
  padding:20px;
  cursor: default;
  /*
  background: #fff url(http://tympanus.net/Tutorials/OriginalHoverEffects/images/bgimg.jpg) repeat;
  */
  -webkit-box-shadow:0 5px 10px #666; 
  -moz-box-shadow:0 5px 10px #666;
  box-shadow:0 5px 10px #666;
  -moz-border-radius:5px;
  -webkit-border-radius:5px;
  -o-border-radius:5px;
  border-radius:5px; 

}

.sign_in_table{
  width:100%;
}

.login_detail{

}

.questions{
  /*
  background-color: white;
  */
}

.question {
  margin:0px 10% 20px 10%;
  padding: 10px 10px 0px 10px;
  background: #fff;


  box-shadow:0 5px 10px #666;

  border-radius:5px;

}

.describe{
    word-wrap:break-word;


}

.answers{
  background-color: yellow;
}

/*
left-fixed 和 right-fixed
要是想要搞成左右中心的话还是不容易的
*/

.right-fixed , .left-fixed{
  position: fixed;
  width: 50px;
  height:200px; 
  background-color: red;
  color:yellow;
  writing-mode: vertical-lr;
  font-size:x-large;
}

.right-fixed {

  right: 0;
  top:20%;


}

.left-fixed {
  left:0;
  top:20%;
}

.submit_result{
  background-color: red;
}

.movies{
  margin:auto;
  width: 80%;

}

.movie {
    float: left;
    width: 300px;
    height: 500px;
    box-shadow: 2px 2px 5px #000;
}

.main_area{

}