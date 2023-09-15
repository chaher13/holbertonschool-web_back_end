export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    }
    throw new TypeError('name must be a string');
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code !== 'string') {
      this._code = code;
    }
    throw new TypeError('code must be a string');
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
