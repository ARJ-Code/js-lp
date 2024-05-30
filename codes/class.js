class Box {
    constructor(value) {
      this.value = value;
    }
  
    // Los métodos se crean en Box.prototype
    getValue() {
      return this.value;
    }
  }
  
  // Definición de la clase hija que hereda de Box
  class ColoredBox extends Box {
    constructor(value, color) {
      // Llama al constructor de la clase padre
      super(value);
      this.color = color;
    }
  
    // Nuevo método específico de ColoredBox
    getColor() {
      return this.color;
    }
  
    // Sobrescribe el método getValue de Box
    getValue() {
      return `Value: ${this.value}, Color: ${this.color}`;
    }
  }
  
  // Ejemplo de uso
  const myBox = new ColoredBox(10, 'red');
  console.log(myBox.getValue());  // Output: Value: 10, Color: red
  console.log(myBox.getColor());  // Output: red
  