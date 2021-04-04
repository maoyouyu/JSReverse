function hook(func) {
  const origin = func;
  return function () {
     console.log(arguments);
     return origin.apply(this, arguments);
  }
}

$.prototype.replaceWith = hook($.prototype.replaceWith);