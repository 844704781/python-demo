function xGtsJason(a) {
    console.log("输入的值:",a)
    function b(t) {
        var H = h[t++]
          , y = -1;
        if (1 != H && 13 != H && 8 != H && 3 != H) {
            y = 0;
            if (28 == h[t]) {
                var J = 1;
                var z = 0;
                for (t++; 2 > z; t++,
                z++)
                    y += (h[t] - 32) * J,
                    J *= 223
            } else if (29 == h[t])
                for (J = 1,
                z = 0,
                t++; 3 > z; t++,
                z++)
                    y += (h[t] - 32) * J,
                    J *= 223;
            else
                y = h[t++] - 32;
            if (2 == H || 4 == H)
                return e = f ? e + ('"' + f[y][1] + '"') : e + '""',
                t
        }
        J = "";
        if (14 != H && 9 != H)
            for (; t < h.length && 27 <= h[t] && 30 != h[t]; t++) {
                z = h[t].toString(2);
                var G = z.match(/^1+?(?=0)/);
                if (G && 8 == z.length) {
                    z = G[0].length;
                    G = h[t].toString(2).slice(7 - z);
                    for (var I = 1; I < z; I++)
                        G += h[I + t].toString(2).slice(2);
                    J += String.fromCharCode(parseInt(G, 2));
                    t += z - 1
                } else
                    27 == h[t] ? (J = "r" == h[t + 1] ? J + "\r" : "n" == h[t + 1] ? J + "\n" : "t" == h[t + 1] ? J + "\t" : J + " ",
                    t++) : J += String.fromCharCode(h[t])
            }
        if (f)
            switch (H) {
            case 14:
            case 9:
                e += '"' + f[y][1] + '"';
                break;
            case 15:
            case 10:
                e = f[y] && f[y][1] && f[y][2] ? e + ('"' + f[y][1] + J + f[y][2] + '"') : e + '""';
                break;
            case 16:
            case 11:
                e += '"' + f[y][1] + J + '"';
                break;
            case 17:
            case 12:
                e += '"' + J + f[y][1] + '"';
                break;
            default:
                e += '"' + J + '"'
            }
        else
            e += '"' + J + '"';
        return t
    }
    function g(t) {
        for (e += "{"; t < h.length; ) {
            t = b(t);
            e += ":";
            switch (h[t]) {
            case 6:
            case 8:
            case 9:
            case 10:
            case 11:
            case 12:
            case 18:
            case 19:
            case 20:
            case 21:
                t = l(t);
                break;
            case 1:
            case 2:
                t = g(t);
                break;
            case 13:
            case 14:
            case 15:
            case 16:
            case 17:
                t = b(t);
                break;
            case 7:
                e += "[]";
                t++;
                break;
            case 5:
                e += "{}";
                t++;
                break;
            default:
                t = m(t)
            }
            if (-1 == t)
                break;
            if (5 == h[t]) {
                e += "}";
                t++;
                break
            } else
                e += ","
        }
        return t
    }
    var f = a, e, h, m = function(t) {
        var H = h[t]
          , y = 0
          , J = 1
          , z = 1
          , G = 1;
        t++;
        switch (H) {
        case 21:
        case 25:
            J = -1;
        case 19:
        case 23:
            z = 100;
            break;
        case 20:
        case 24:
            J = -1;
            break;
        case 30:
            return e += "null",
            t
        }
        if (26 == h[t]) {
            y = h[t + 1];
            y -= 32;
            G = 10;
            for (H = 1; H < y; H++)
                G *= 10;
            y = h[t + 1] - 32;
            t += 2
        }
        H = h[t] - 32;
        var I = 223;
        for (t++; 32 <= h[t]; t++)
            H += (h[t] - 32) * I,
            I *= 223;
        H *= z;
        -1 == J && (H *= -1);
        e = 0 == y ? e + H : e + (H / G).toFixed(y);
        return t
    }, l = function(t) {
        e += "[";
        switch (h[t]) {
        case 6:
            t++;
            if (7 == h[t])
                return t++,
                e += "]",
                t;
            break;
        case 8:
        case 9:
        case 10:
        case 11:
        case 12:
            t = b(t);
            if (-1 == t)
                return -1;
            if (7 == h[t])
                return e += "]",
                t++,
                t;
            e += ",";
            break;
        case 18:
        case 19:
        case 20:
        case 21:
            t = m(t);
            if (-1 == t)
                return -1;
            if (7 == h[t])
                return e += "]",
                t++,
                t;
            e += ",";
            break;
        case 7:
            return e += "[]",
            t++,
            t;
        case 5:
            return e += "{}",
            t++,
            t;
        default:
            return t
        }
        for (; t < h.length; ) {
            switch (h[t]) {
            case 6:
            case 8:
            case 9:
            case 10:
            case 11:
            case 12:
            case 18:
            case 19:
            case 20:
            case 21:
                t = l(t);
                break;
            case 1:
            case 2:
                t = g(t);
                break;
            case 13:
            case 14:
            case 15:
            case 16:
            case 17:
                t = b(t);
                break;
            case 7:
                e += "[]";
                t++;
                break;
            case 5:
                e += "{}";
                t++;
                break;
            default:
                t = m(t)
            }
            if (-1 == t)
                break;
            if (7 == h[t])
                return e += "]",
                t++,
                t;
            e += ","
        }
        return -1
    };
    this.decompress_json = function(t) {
        e = "";
        h = t;
        for (t = 0; t < h.length; t++) {
            if (6 == h[t])
                t = l(t);
            else if (1 == h[t] || 2 == h[t])
                t = g(t);
            if (-1 == t)
                break
        }
        return e
    }
    ;
    var n = function(t, H) {
        for (var y = 0; y < H; y++)
            if (13 == t[y] || 10 == t[y] || 9 == t[y]) {
                for (var J = H; J > y; J--)
                    t[J] = t[J - 1];
                t[y + 1] = 13 == t[y] ? "r" : 10 == t[y] ? "n" : 9 == t[y] ? "t" : " ";
                t[y] = 27;
                H++
            }
        return H
    }
      , p = function(t) {
        if (223 > t)
            e.push(t + 32);
        else
            for (49729 > t ? e.push(28) : e.push(29),
            offset = 1; 0 < t; offset++)
                e.push(t % 223 + 32),
                t = parseInt(t / 223)
    }
      , q = function(t) {
        for (var H = 0; H < t.length; H++)
            e.push(t[H])
    }
      , v = function(t, H) {
        if (3 <= t.length) {
            if (f) {
                if (f.s && f.s.key && null != f.s[t] && (H = f.s[t],
                -1 != H))
                    return p(H),
                    14;
                if (f.h)
                    for (H = 0; H < f.h.length; H++) {
                        var y = f[f.h[H]][1].length;
                        if (t.substr(0, y) == f[f.h[H]][1])
                            return p(f.h[H]),
                            q(B(t.substr(y))),
                            n(e),
                            16
                    }
                if (f.t)
                    for (H = 0; H < f.t.length; H++)
                        if (y = f[f.t[H]][1].length,
                        t.length >= y && t.substr(t.length - y) == f[f.t[H]][1])
                            return p(f.t[H]),
                            q(B(t.substr(0, t.length - y))),
                            n(e),
                            17;
                if (f.ht)
                    for (H = 0; H < f.ht.length; H++) {
                        var J = f[f.ht[H]][1]
                          , z = f[f.ht[H]][2]
                          , G = J.length;
                        y = z.length;
                        if (t.length > G && t.substr(0, G) == J && t.length > y && t.substr(t.length - y) == z)
                            return p(f.ht[H]),
                            q(B(t.substr(G, t.length - y - G))),
                            n(e),
                            15
                    }
            }
            q(B(t));
            n(e)
        } else
            q(B(t));
        return 13
    }
      , u = function(t) {
        for (; t < h.length && (" " == h[t] || "\t" == h[t] || "\r" == h[t] || "\n" == h[t]); t++)
            ;
        return t
    }
      , C = function(t, H) {
        var y = H;
        for (H++; H < h.length; H++)
            if ('"' == h[H]) {
                var J = e.length;
                e.push(0);
                H++;
                y = v(h.substr(y + 1, H - y - 2), H);
                if ("[" == t)
                    switch (y) {
                    case 16:
                        e[J] = 11;
                        break;
                    case 17:
                        e[J] = 12;
                        break;
                    case 15:
                        e[J] = 10;
                        break;
                    case 14:
                        e[J] = 9;
                        break;
                    default:
                        e[J] = 8
                    }
                else
                    e[J] = y;
                return H
            }
        return -1
    }
      , D = function(t, H) {
        H = u(H);
        if ("null" == h.substr(H, 4))
            return "[" == t && e.push(6),
            e.push(30),
            H + 4;
        var y = H
          , J = 0
          , z = 0
          , G = 1;
        for ("-" == h[H] && (G = -1); H < h.length; H++)
            if ("." == h[H] ? (J = 1,
            y = H + 1) : J && (J *= 10,
            z++),
            "," == h[H] || "}" == h[H] || "]" == h[H]) {
                var I = parseInt(h.substr(y, H - y));
                J && z && (0 > I && (I *= -1),
                I *= J / 10,
                I += parseInt(h.substr(y)));
                "[" == t ? 0 > G ? (0 > I && (I *= -1),
                0 == I % 100 ? (e.push(21),
                I = parseInt(I / 100)) : e.push(20)) : 0 == I % 100 ? (e.push(19),
                I = parseInt(I / 100)) : e.push(18) : 0 > G ? (0 > I && (I *= -1),
                0 == I % 100 ? (e.push(25),
                I = parseInt(I / 100)) : e.push(24)) : 0 == I % 100 ? (e.push(23),
                I = parseInt(I / 100)) : e.push(22);
                J && z && (e.push(26),
                e.push(32 + z - 1));
                for (t = 0; e.push(32 + I % 223),
                I = parseInt(I / 223),
                0 != I; t++)
                    ;
                return H
            }
        return -1
    }
      , E = function(t) {
        t = u(t);
        var H = "[";
        if ("]" == h[t])
            return e.push(6),
            e.push(7),
            t++,
            t;
        for (; t < h.length; ) {
            "[" == h[t] ? (t++,
            "[" == H && e.push(6),
            t = E(t)) : "{" == h[t] ? (t++,
            "[" == H && e.push(6),
            t = x(t)) : t = '"' == h[t] ? C(H, t) : D(H, t);
            if (-1 == t)
                break;
            H = 0;
            t = u(t);
            if ("," == h[t])
                t++,
                t = u(t);
            else {
                if ("]" == h[t])
                    return t++,
                    e.push(7),
                    t;
                break
            }
        }
        return -1
    }
      , x = function(t) {
        var H = "{";
        var y = t;
        if ("}" == h[t])
            return e.push(5),
            t++,
            t;
        for (t++; t < h.length; t++)
            if ('"' == h[t]) {
                var J = e.length;
                e.push(0);
                t++;
                y = h.substr(y + 1, t - y - 2);
                y = v(y, t);
                if ("{" == H)
                    switch (y) {
                    case 15:
                    case 16:
                    case 17:
                    case 14:
                        e[J] = 2;
                        break;
                    default:
                        e[J] = 1
                    }
                else
                    switch (y) {
                    case 15:
                    case 16:
                    case 17:
                    case 14:
                        e[J] = 4;
                        break;
                    default:
                        e[J] = 3
                    }
                t = u(t);
                if (":" != h[t])
                    break;
                t++;
                t = u(t);
                "[" == h[t] ? (t++,
                t = E(t)) : "{" == h[t] ? (t++,
                t = x(t)) : t = '"' == h[t] ? C(":", t) : D(":", t);
                if (-1 == t)
                    break;
                H = 0;
                t = u(t);
                if ("," == h[t]) {
                    t++;
                    t = u(t);
                    if ('"' != h[t])
                        break;
                    y = t
                } else {
                    if ("}" == h[t])
                        return t++,
                        e.push(5),
                        t;
                    break
                }
            }
        return -1
    };
    this.compress_json = function(t, H) {
        if (null == H || 0 > H)
            H = 0;
        var y = 0;
        h = t;
        for (e = []; y < h.length; y++)
            if ("[" == h[y] ? (y++,
            y = E(y)) : "{" == h[y] && (y++,
            y = x(y)),
            -1 == y)
                return null;
        t = new ArrayBuffer(e.length + H);
        t = new Uint8Array(t);
        for (y = 0; y < e.length; y++)
            t[y + H] = e[y] % 255;
        return t
    }
    ;
    var B = function(t) {
        for (var H = [], y, J = 0; J < t.length; J++)
            y = t.charCodeAt(J),
            65536 <= y && 1114111 >= y ? (H.push(y >> 18 & 7 | 240),
            H.push(y >> 12 & 63 | 128),
            H.push(y >> 6 & 63 | 128),
            H.push(y & 63 | 128)) : 2048 <= y && 65535 >= y ? (H.push(y >> 12 & 15 | 224),
            H.push(y >> 6 & 63 | 128),
            H.push(y & 63 | 128)) : 128 <= y && 2047 >= y ? (H.push(y >> 6 & 31 | 192),
            H.push(y & 63 | 128)) : H.push(y & 255);
        return H
    };
    (function() {
        if (f && null == f.s)
            for (var t = 0; t < f.length; t++)
                switch (f[t][0]) {
                case 0:
                    null == f.s && (f.s = {});
                    null == f.s[f[t][1]] && (f.s[f[t][1]] = t);
                    break;
                case 1:
                    null == f.h && (f.h = []);
                    f.h.push(t);
                    break;
                case 2:
                    null == f.t && (f.t = []);
                    f.t.push(t);
                    break;
                case 3:
                    null == f.ht && (f.ht = []);
                    f.ht.push(t);
                    break;
                case 4:
                    null == f.a && (f.a = []),
                    f.a.push(t)
                }
    }
    )()
}

function my_decode(data,buffer){
    return (new xGtsJason(data)).decompress_json(buffer)
}
