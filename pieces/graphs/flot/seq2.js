// <script src='http://spencertipping.com/montenegro/montenegro.client.js'></script>

// This is how I would write it (modulo some line-joining and general compactness):
$(caterwaul.clone('std seq montenegro')(function () {
  let[ns = [1, 2, 3, 4, 5],
      ps = [6, 7, 8];

      options = {...}] in
  seq[~ns *!~n[~ps *!p[
    let[key = 'n#{n}p0#{p}',
        colors = ['#fc0', '#ff0', '#7c0'],
        labels = ['N = #{n}, P = #{p}', 'Normal', 'Skew-normal'],
        series(data, label, color, bars) =
          {data: data, label: label, color: color,
           bars: bars ? {show: true} : false, lines: {show: true}}] in

    $ /se[_('body').append(html[div.chart /attr('id', 'chart-n#{n}-p#{p}') /css({width: 900, height: 600})]),
          _.plot('element', seq[~[binomial, sn, normal] *[series(_[key], labels[_i], colors[_i], _i === 0)]], options)]]]];
}));
