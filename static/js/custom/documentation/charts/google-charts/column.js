"use strict";var KTGoogleChartColumnDemo={init:function(){google.load("visualization","1",{packages:["corechart","bar","line"]}),google.setOnLoadCallback((function(){var o=new google.visualization.DataTable;o.addColumn("timeofday","Time of Day"),o.addColumn("number","Motivation Level"),o.addColumn("number","Energy Level"),o.addRows([[{v:[8,0,0],f:"8 am"},1,.25],[{v:[9,0,0],f:"9 am"},2,.5],[{v:[10,0,0],f:"10 am"},3,1],[{v:[11,0,0],f:"11 am"},4,2.25],[{v:[12,0,0],f:"12 pm"},5,2.25],[{v:[13,0,0],f:"1 pm"},6,3],[{v:[14,0,0],f:"2 pm"},7,4],[{v:[15,0,0],f:"3 pm"},8,5.25],[{v:[16,0,0],f:"4 pm"},9,7.5],[{v:[17,0,0],f:"5 pm"},10,10]]),new google.visualization.ColumnChart(document.getElementById("kt_docs_google_chart_column")).draw(o,{title:"Motivation and Energy Level Throughout the Day",focusTarget:"category",hAxis:{title:"Time of Day",format:"h:mm a",viewWindow:{min:[7,30,0],max:[17,30,0]}},vAxis:{title:"Rating (scale of 1-10)"},colors:["#6e4ff5","#fe3995"]})}))}};KTUtil.onDOMContentLoaded((function(){KTGoogleChartColumnDemo.init()}));
