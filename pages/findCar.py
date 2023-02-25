# The 'findCar.py' redirects to the interactive and custom filtering built using elasticsearch

import pathlib
from dash.dependencies import Input, Output, State
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()


app.scripts.config.serve_locally = True

d1Head = html.Div([
    html.Header(
            dbc.Container(
                html.Div(
                    dbc.Row(
                        dbc.Col(
                            [html.H1(
                                [
                                    html.Img(src="data:image/png;base64,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",
                                           className="page-header-icon", alt="headIcon"),
                                    " Interactive dashboard"
                                ],
                                className="page-header-title"
                            ),
                            html.Div(
                                "Make it interactive -",

                                className="page-header-subtitle"
                            )
                            ],
                            className="col-auto mt-4"
                        ),
                        className="row align-items-center justify-content-between"
                    ),
                    className="pt-4"
                ),
                className="px-4"
            ),
            className="page-header page-header-dark bg-gradient-primary-to-secondary pb-10 m-4"
    )
])

dashbrd = html.Div([
    d1Head,
    html.Center(
        html.Iframe(src="https://engage.kb.us-central1.gcp.cloud.es.io:9243/app/dashboards#/view/d80aa910-de50-11ec"
                        "-8bcb-2b59f6170ad5?embed=true&_g=(filters:!(),refreshInterval:(pause:!t,value:0),"
                        "time:(from:now-15m,to:now))&_a=(description:'',filters:!(('$state':(store:appState),"
                        "meta:(alias:!n,controlledBy:'1653720067959',disabled:!f,field:ExShowroomPrice,"
                        "index:'772b5040-de50-11ec-8bcb-2b59f6170ad5',key:ExShowroomPrice,negate:!f,params:(gte:4222,"
                        "lte:212155397),type:range),query:(range:(ExShowroomPrice:(gte:4222,lte:212155397))))),"
                        "fullScreenMode:!f,options:(hidePanelTitles:!f,syncColors:!f,useMargins:!t),panels:!(("
                        "embeddableConfig:(enhancements:(),hidePanelTitles:!f,savedVis:(data:(aggs:!(),searchSource:("
                        "filter:!(),query:(language:kuery,query:''))),description:'',id:'',params:(controls:!(("
                        "fieldName:Make,id:'1653719964211',indexPattern:'772b5040-de50-11ec-8bcb-2b59f6170ad5',"
                        "label:Make,options:(dynamicOptions:!t,multiselect:!t,order:desc,size:5,type:terms),"
                        "parent:'',type:list),(fieldName:BodyType,id:'1653719984409',"
                        "indexPattern:'772b5040-de50-11ec-8bcb-2b59f6170ad5',label:'Body%20Type',"
                        "options:(dynamicOptions:!t,multiselect:!t,order:desc,size:5,type:terms),parent:'',"
                        "type:list),(fieldName:FuelType,id:'1653720010828',"
                        "indexPattern:'772b5040-de50-11ec-8bcb-2b59f6170ad5',label:'Fuel%20Type',"
                        "options:(dynamicOptions:!t,multiselect:!t,order:desc,size:5,type:terms),parent:'',"
                        "type:list)),pinFilters:!f,updateFiltersOnChange:!t,useTimeFilter:!f),title:'',"
                        "type:input_control_vis,uiState:())),gridData:(h:6,i:'3ea2c083-daae-4482-8c19-afb592b10019',"
                        "w:48,x:0,y:0),panelIndex:'3ea2c083-daae-4482-8c19-afb592b10019',title:Filter,"
                        "type:visualization,version:'8.2.2'),(embeddableConfig:(enhancements:(),hidePanelTitles:!f,"
                        "savedVis:(data:(aggs:!(),searchSource:(filter:!(),query:(language:kuery,query:''))),"
                        "description:'',id:'',params:(controls:!((fieldName:ExShowroomPrice,id:'1653720067959',"
                        "indexPattern:'772b5040-de50-11ec-8bcb-2b59f6170ad5',label:Price,options:(decimalPlaces:0,"
                        "step:299999),parent:'',type:range),(fieldName:Cylinders,id:'1653720094220',"
                        "indexPattern:'772b5040-de50-11ec-8bcb-2b59f6170ad5',label:Cylinders,"
                        "options:(decimalPlaces:0,step:1),parent:'',type:range)),pinFilters:!f,"
                        "updateFiltersOnChange:!t,useTimeFilter:!f),title:'',type:input_control_vis,uiState:())),"
                        "gridData:(h:6,i:'6d6cafb8-f0c2-43f8-b720-0ccf16a20070',w:48,x:0,y:6),"
                        "panelIndex:'6d6cafb8-f0c2-43f8-b720-0ccf16a20070',title:Filter,type:visualization,"
                        "version:'8.2.2'),(embeddableConfig:(attributes:(references:!(("
                        "id:'772b5040-de50-11ec-8bcb-2b59f6170ad5',name:indexpattern-datasource-current-indexpattern,"
                        "type:index-pattern),(id:'772b5040-de50-11ec-8bcb-2b59f6170ad5',"
                        "name:indexpattern-datasource-layer-f655dd55-1eff-4c2e-88dc-260446098cf0,"
                        "type:index-pattern)),state:(datasourceStates:(indexpattern:(layers:("
                        "f655dd55-1eff-4c2e-88dc-260446098cf0:(columnOrder:!('7c39ae08-7b22-46c7-9010-1b4a81d999f8',"
                        "'148dce00-6c2c-40d4-982e-5662a69f9530'),columns:('148dce00-6c2c-40d4-982e-5662a69f9530':("
                        "dataType:number,isBucketed:!f,label:'Unique%20count%20of%20Model',"
                        "operationType:unique_count,params:(emptyAsNull:!t),scale:ratio,sourceField:Model),"
                        "'7c39ae08-7b22-46c7-9010-1b4a81d999f8':(dataType:string,isBucketed:!t,"
                        "label:'Top%205%20values%20of%20Make',operationType:terms,params:(missingBucket:!f,"
                        "orderBy:(columnId:'148dce00-6c2c-40d4-982e-5662a69f9530',type:column),orderDirection:desc,"
                        "otherBucket:!t,parentFormat:(id:terms),size:5),scale:ordinal,sourceField:Make)),"
                        "incompleteColumns:())))),filters:!(),query:(language:kuery,query:''),visualization:("
                        "layers:!((accessors:!('148dce00-6c2c-40d4-982e-5662a69f9530'),"
                        "layerId:f655dd55-1eff-4c2e-88dc-260446098cf0,layerType:data,position:top,"
                        "seriesType:bar_stacked,showGridlines:!f,xAccessor:'7c39ae08-7b22-46c7-9010-1b4a81d999f8',"
                        "yConfig:!((color:%23e07833,forAccessor:'148dce00-6c2c-40d4-982e-5662a69f9530')))),"
                        "legend:(isVisible:!t,position:right),preferredSeriesType:bar_stacked,"
                        "title:'Empty%20XY%20chart',valueLabels:hide)),title:'',type:lens,visualizationType:lnsXY),"
                        "enhancements:(),hidePanelTitles:!f),gridData:(h:15,i:c070d7db-c990-4bd4-8203-cd5b9ddfa1f5,"
                        "w:24,x:0,y:12),panelIndex:c070d7db-c990-4bd4-8203-cd5b9ddfa1f5,"
                        "title:'Make%20by%20Model%20Count',type:lens,version:'8.2.2'),(embeddableConfig:(attributes:("
                        "references:!((id:'772b5040-de50-11ec-8bcb-2b59f6170ad5',"
                        "name:indexpattern-datasource-current-indexpattern,type:index-pattern),"
                        "(id:'772b5040-de50-11ec-8bcb-2b59f6170ad5',"
                        "name:indexpattern-datasource-layer-4599c83c-52ba-4708-ab1a-ed7f799b0ff7,"
                        "type:index-pattern)),state:(datasourceStates:(indexpattern:(layers:("
                        "'4599c83c-52ba-4708-ab1a-ed7f799b0ff7':(columnOrder:!("
                        "'6b528e95-b7d5-43b2-ba19-e2d3a8019798','9207eeaa-4271-4ea4-9ba3-f6e16a431ba1'),"
                        "columns:('6b528e95-b7d5-43b2-ba19-e2d3a8019798':(dataType:string,isBucketed:!t,"
                        "label:'Top%205%20values%20of%20Make',operationType:terms,params:(missingBucket:!f,"
                        "orderBy:(columnId:'9207eeaa-4271-4ea4-9ba3-f6e16a431ba1',type:column),orderDirection:asc,"
                        "otherBucket:!t,parentFormat:(id:terms),size:5),scale:ordinal,sourceField:Make),"
                        "'9207eeaa-4271-4ea4-9ba3-f6e16a431ba1':(dataType:number,isBucketed:!f,"
                        "label:'Median%20of%20ExShowroomPrice',operationType:median,params:(emptyAsNull:!t),"
                        "scale:ratio,sourceField:ExShowroomPrice)),incompleteColumns:())))),filters:!(),"
                        "query:(language:kuery,query:''),visualization:(layers:!((accessors:!("
                        "'9207eeaa-4271-4ea4-9ba3-f6e16a431ba1'),layerId:'4599c83c-52ba-4708-ab1a-ed7f799b0ff7',"
                        "layerType:data,position:top,seriesType:bar_horizontal,showGridlines:!f,"
                        "xAccessor:'6b528e95-b7d5-43b2-ba19-e2d3a8019798',yConfig:!((color:%23d36086,"
                        "forAccessor:'9207eeaa-4271-4ea4-9ba3-f6e16a431ba1')))),legend:(isVisible:!t,position:right),"
                        "preferredSeriesType:bar_horizontal,title:'Empty%20XY%20chart',valueLabels:hide)),title:'',"
                        "type:lens,visualizationType:lnsXY),enhancements:(),hidePanelTitles:!f),gridData:(h:15,"
                        "i:'76f866be-ebc9-4617-a035-7647e4786603',w:24,x:24,y:12),"
                        "panelIndex:'76f866be-ebc9-4617-a035-7647e4786603',title:'Make%20by%20Median%20Price',"
                        "type:lens,version:'8.2.2'),(embeddableConfig:(enhancements:()),gridData:(h:22,"
                        "i:add14e34-76e0-4bc2-b71f-83a488fbc6c0,w:48,x:0,y:27),"
                        "id:baf9b640-de50-11ec-8bcb-2b59f6170ad5,panelIndex:add14e34-76e0-4bc2-b71f-83a488fbc6c0,"
                        "type:search,version:'8.2.2')),query:(language:kuery,query:''),tags:!(),timeRestore:!f,"
                        "title:carsDBFinal,viewMode:view)",
                    style={"height": "75vh", "width": "70vw", "display":"block"},
                    title="elasticDashBoard"),
    ),

], className="mx-4")

