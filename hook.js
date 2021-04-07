function hook(func) {
    const origin = func;
    return function () {
        console.log(arguments);
        return origin.apply(this, arguments);
    }
}

// 这里的 replaceWith 可以替换成任何你需要的 方法。
$.prototype.cookie = hook($.prototype.cookie);

/////////////////////////////////////////////////////////
(
    function () {
        'use strict';
        Object.defineProperty(
            document, 'cookie', {
                set: function (cookie) {
                    if (cookie.indexOf('RM4hZBv0dDon443M') != -1) {
                        debugger;
                    }
                    return cookie;
                }
            }
        )
    }
)();

///////////////////////hook window _$pr 属性赋值的地方，看看赋值什么内容///////////////////////////
(function () {
    Object.defineProperty(window, '_$pr', {
        get: function (hashvalue) {
            debugger;
            console.log(hashvalue);
            return hashvalue
        }
    })
})();


/////////////////////////////hook b函数 打印b函数加密前和加密后的内容分别是什么
(function () {
    var new_g = g;
    g = function (e) {
        var retval = new_g(e);
        console.log('加密前时间戳为：', e, '加密后时间戳为：', retval);
        return retval;
    }
})