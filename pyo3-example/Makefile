init:
	maturin init 

build: 
	cargo build --release
	cp target/release/libpyo3_example.dylib libpyo3_example.so

clean:
	cargo clean
	rm -f libpyo3_example.so