const urls = ["/get-json"];

Promise.all(urls.map(url => d3.json(url))).then(run);

function run(data) {
    console.log(data[0])
    ForceGraph(data[0], {
        nodeId: d => d.id,
        nodeGroup: d => d.group,
        nodeTitle: d => `${d.id}\n${d.group}`,
        linkStrokeWidth: l => Math.sqrt(l.value),
        width: 640,
        height: 600 //,
        //invalidation // a promise to stop the simulation when the cell is re-run
        })
};
