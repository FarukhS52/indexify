from indexify import IndexifyClient, ExtractionGraph

client = IndexifyClient()

extraction_graph_spec = """
name: 'pdfqa'
extraction_policies:
  - extractor: 'tensorlake/marker'
    name: 'pdf_to_text'
  - extractor: 'tensorlake/chunk-extractor'
    name: 'text_to_chunk'
    input_params:
      text_splitter: 'recursive'
      chunk_size: 500
      overlap: 0
    content_source: 'pdf_to_text'
  - extractor: 'tensorlake/minilm-l6'
    name: 'chunk_to_embedding'
    content_source: 'text_to_chunk'
"""

extraction_graph = ExtractionGraph.from_yaml(extraction_graph_spec)
client.create_extraction_graph(extraction_graph)