$ () ->
  $ document
    .ready () ->

      Highcharts.setOptions
        global: 
          useUTC: false

      $ '#container' 
        .highcharts 'StockChart',
          chart: 
            marginRight: 10,
            events: 
              load:  () ->
                window.series = this.series[0]
                console.log 123
          xAxis:
            type: 'datetime'
            tickPixelInterval: 150
            minRange: 10000
          yAxis: 
            title: 
              text: 'Value'
            plotLines: [{
              value: 0
              width: 1
              color: '#808080'
            }]
          tooltip: 
            formatter:  () ->
              return '<b>' + this.series.name + '</b><br/>' +
                Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                Highcharts.numberFormat(this.y, 2)
          legend: 
            enabled: false
          exporting: 
            enabled: false
          series: [{
            name: 'Random data',
            data: []     
          }]

      return

  return
  

