function urldecode(str)
  return str:gsub("%%(%x%x)", function(h)
    return string.char(tonumber(h, 16))
  end)
end

local function file_exists(path)
  local f = io.open(path, "rb")
  if f then f:close(); return true else return false end
end

local function resolve_path(src)
  local try_paths = { src, "Assets/" .. src, "Excalidraw/" .. src }
  for _, p in ipairs(try_paths) do
    if file_exists(p) then return p end
  end
end

local function inline_image(src)
  src = urldecode(src)
  local resolved = resolve_path(src)
  if not resolved then
    return src
  end

  local f = io.open(resolved, "rb")
  if not f then
    return src -- return unchanged element if not resolved
  end

  local img = f:read("*all")
  f:close()

  local ext = resolved:match("%.([^./]+)$") or "png"
  local mime = "image/" .. ext
  local b64 = pandoc.pipe("base64", {}, img)
  return "data:" .. mime .. ";base64," .. b64
end

function Image(el)
  el.src = inline_image(el.src)
  return el
end
