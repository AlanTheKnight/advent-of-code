const data = require("fs").readFileSync("input/day7.input.txt", { encoding: "utf-8" });

let cwd = [], d = [];
const f = new Map();
f.set("/", 0);

for (const line of data.split("\n")) {
    if (line.startsWith("$")) {
        if (line.startsWith("$ cd")) {
            const nd = line.split(" ").slice(-1);
            if (nd == "..") cwd.pop();
            else cwd.push(nd);
        } else d = [];
    } else {
        const k = cwd.join();
        if (line.startsWith("dir"))
            f.set(k + "," + line.split(" ").slice(-1), 0);
        else {
            let [s, _] = line.split(" ");
            f.set(k, parseInt(s) + (f.has(k) ? f.get(k) : 0));
        }
    }
}

const nf = new Map(f);
for (const i of f.keys()) {
    const subd = Array.from(f.keys()).filter(x => x.startsWith(i) && x != i).map(x => f.get(x));
    const bs = subd.length ? subd.reduce((p, c) => p += c) : 0;
    nf.set(i, f.get(i) + bs);
}

console.log("Part 1:", Array.from(nf.values()).filter(x => x <= 100000).reduce((p, c) => p += c));

const space = 30000000 - 70000000 + nf.get("/");
console.log("Part 2:", Array.from(nf.values()).filter(x => x >= space).sort()[0]);
