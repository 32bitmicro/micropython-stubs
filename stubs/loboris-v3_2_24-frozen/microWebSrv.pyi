from typing import Any

class MicroWebSrvRoute:
    route: Any
    method: Any
    func: Any
    routeArgNames: Any
    routeRegex: Any
    def __init__(self, route, method, func, routeArgNames, routeRegex) -> None: ...

class MicroWebSrv:
    _indexPages: Any
    _mimeTypes: Any
    _html_escape_chars: Any
    _pyhtmlPagesExt: str
    _docoratedRouteHandlers: Any
    @classmethod
    def route(cls, url, method: str = ...): ...
    @staticmethod
    def HTMLEscape(s): ...
    @staticmethod
    def _tryAllocByteArray(size): ...
    @staticmethod
    def _tryStartThread(func, args=..., stacksize: int = ...): ...
    @staticmethod
    def _unquote(s): ...
    @staticmethod
    def _unquote_plus(s): ...
    @staticmethod
    def _fileExists(path): ...
    @staticmethod
    def _isPyHTMLFile(filename): ...
    _srvAddr: Any
    _webPath: Any
    _notFoundUrl: Any
    _started: bool
    thID: Any
    isThreaded: bool
    _state: str
    MaxWebSocketRecvLen: int
    WebSocketThreaded: bool
    WebSocketStackSize: int
    AcceptWebSocketCallback: Any
    _routeHandlers: Any
    def __init__(self, routeHandlers=..., port: int = ..., bindIP: str = ..., webPath: str = ...) -> None: ...
    def _serverProcess(self) -> None: ...
    _server: Any
    def Start(self, threaded: bool = ..., stackSize: int = ...) -> None: ...
    def Stop(self) -> None: ...
    def IsStarted(self): ...
    def threadID(self): ...
    def State(self): ...
    def SetNotFoundPageUrl(self, url: Any | None = ...) -> None: ...
    def GetMimeTypeFromFilename(self, filename): ...
    def GetRouteHandler(self, resUrl, method): ...
    def _physPathFromURLPath(self, urlPath): ...
    class _client:
        _microWebSrv: Any
        _socket: Any
        _addr: Any
        _method: Any
        _path: Any
        _httpVer: Any
        _resPath: str
        _queryString: str
        _queryParams: Any
        _headers: Any
        _contentType: Any
        _contentLength: int
        def __init__(self, microWebSrv, socket, addr) -> None: ...
        def _processRequest(self) -> None: ...
        def _parseFirstLine(self, response): ...
        def _parseHeader(self, response): ...
        def _getConnUpgrade(self): ...
        def GetServer(self): ...
        def GetAddr(self): ...
        def GetIPAddr(self): ...
        def GetPort(self): ...
        def GetRequestMethod(self): ...
        def GetRequestTotalPath(self): ...
        def GetRequestPath(self): ...
        def GetRequestQueryString(self): ...
        def GetRequestQueryParams(self): ...
        def GetRequestHeaders(self): ...
        def GetRequestContentType(self): ...
        def GetRequestContentLength(self): ...
        def ReadRequestContent(self, size: Any | None = ...): ...
        def ReadRequestPostedFormData(self): ...
        def ReadRequestContentAsJSON(self): ...
    class _response:
        _client: Any
        def __init__(self, client) -> None: ...
        def _write(self, data): ...
        def _writeFirstLine(self, code) -> None: ...
        def _writeHeader(self, name, value) -> None: ...
        def _writeContentTypeHeader(self, contentType, charset: Any | None = ...) -> None: ...
        def _writeServerHeader(self) -> None: ...
        def _writeEndHeader(self) -> None: ...
        def _writeBeforeContent(self, code, headers, contentType, contentCharset, contentLength) -> None: ...
        def WriteSwitchProto(self, upgrade, headers: Any | None = ...) -> None: ...
        def WriteResponse(self, code, headers, contentType, contentCharset, content): ...
        def WriteResponsePyHTMLFile(self, filepath, headers: Any | None = ...): ...
        def WriteResponseFile(self, filepath, contentType: Any | None = ..., headers: Any | None = ...): ...
        def WriteResponseFileAttachment(self, filepath, attachmentName, headers: Any | None = ...): ...
        def WriteResponseOk(
            self, headers: Any | None = ..., contentType: Any | None = ..., contentCharset: Any | None = ..., content: Any | None = ...
        ): ...
        def WriteResponseJSONOk(self, obj: Any | None = ..., headers: Any | None = ...): ...
        def WriteResponseRedirect(self, location): ...
        def WriteResponseError(self, code): ...
        def WriteResponseJSONError(self, code, obj: Any | None = ...): ...
        def WriteResponseBadRequest(self): ...
        def WriteResponseForbidden(self): ...
        def WriteResponseNotFound(self): ...
        def WriteResponseMethodNotAllowed(self): ...
        def WriteResponseInternalServerError(self): ...
        def WriteResponseNotImplemented(self): ...
        _errCtnTmpl: str
        _execErrCtnTmpl: str
        _responseCodes: Any