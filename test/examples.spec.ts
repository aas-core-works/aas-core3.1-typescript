import * as AasTypes from "../src/types";

test("types match", () => {
  // Create a property
  const aProperty = new AasTypes.Property(AasTypes.DataTypeDefXsd.Int);

  // Create a blob
  const aBlob = new AasTypes.Blob(
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    null,
    "text/plain"
  );

  // Create another property
  const anotherProperty = new AasTypes.Property(AasTypes.DataTypeDefXsd.Decimal);

  // Check the type matches

  expect(AasTypes.typesMatch(aProperty, aProperty)).toStrictEqual(true);

  expect(AasTypes.typesMatch(aProperty, aBlob)).toStrictEqual(false);

  expect(AasTypes.typesMatch(aProperty, anotherProperty)).toStrictEqual(true);
});
