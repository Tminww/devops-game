from lazydocs import generate_docs

# The parameters of this function correspond to the CLI options
generate_docs(
    paths=[
        "./src/",
    ],
    output_path="./docs",
)
