export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code === "string") {
      this._code = code;
    }
    throw new TypeError("code must be a string");
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === "string") {
      this._name = name;
    }
    throw new TypeError("name must be a string");
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
