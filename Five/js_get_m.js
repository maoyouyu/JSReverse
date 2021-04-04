window = {}

function get_data_value() {
    var f = Date.parse(new Date());
    var f = 1617431182000;
    var m = get_m_value(f)
    return m

}

function get_m_value(date_time) {
    var m_value = _0x499969(_0x1ee7ec(unescape(encodeURIComponent(date_time))))
    return m_value
}

function _0x1ee7ec(_0x206333) {
    // return _0x12b47d(_0x11a7a2(_0x35f5f2(_0x206333), 8 * _0x206333[_$UH[108]]));
    return _0x12b47d(_0x11a7a2(_0x35f5f2(_0x206333), 8 * _0x206333["length"]));
}

function _0x499969(time_str) {
    var _0x5bdda4, _0x322a73, _0xd0b5cd = '0123456789abcdef', _0x21f411 = '';
    for (_0x322a73 = 0; _0x322a73 < time_str["length"]; _0x322a73 += 1) {
        _0x5bdda4 = time_str["charCodeAt"](_0x322a73),
            _0x21f411 += _0xd0b5cd['charAt'](_0x5bdda4 >>> 4 & 15) + _0xd0b5cd['charAt'](15 & _0x5bdda4)
    }
    ;
    return _0x21f411;
}

function _0x35f5f2(local$$1393) {
    var local$$1395;
    /** @type {!Array} */
    var local$$1398 = [];
    local$$1398[(local$$1393[_$UH[108]] >> 2) - 1] = void 0;
    /** @type {number} */
    local$$1395 = 0;
    for (; local$$1395 < local$$1398[_$UH[108]]; local$$1395 = local$$1395 + 1) {
        /** @type {number} */
        local$$1398[local$$1395] = 0;
    }
    /** @type {number} */
    var local$$1434 = 8 * local$$1393[_$UH[108]];
    /** @type {number} */
    local$$1395 = 0;
    for (; local$$1395 < local$$1434; local$$1395 = local$$1395 + 8) {
        local$$1398[local$$1395 >> 5] |= (255 & local$$1393[_$UH[15]](local$$1395 / 8)) << local$$1395 % 32;
    }
    return local$$1398;
}