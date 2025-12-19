-- Remove non-visible / structural elements
function Div(el)
  local classes = el.classes
  local id = el.identifier

  -- EPUB nav, headers, footers, metadata containers
  for _, class in ipairs(classes) do
    if class == "nav"
       or class == "toc"
       or class == "metadata"
       or class == "header"
       or class == "footer" then
      return {}
    end
  end

  -- Common EPUB IDs
  if id == "toc" or id == "nav" then
    return {}
  end

  return el
end

-- Remove Raw HTML blocks entirely
function RawBlock(el)
  return {}
end

-- Remove comments
function Comment(el)
  return {}
end
