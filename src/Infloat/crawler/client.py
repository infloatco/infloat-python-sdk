# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.website_ingestion_response import WebsiteIngestionResponse
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.youtube_transcript import YoutubeTranscript
from .. import core
from ..types.file_path_response import FilePathResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CrawlerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def crawl_website(
        self,
        *,
        url: str,
        chatbot_id: str,
        max_depth: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteIngestionResponse:
        """
        Start a website crawl.

        Parameters
        ----------
        url : str

        chatbot_id : str

        max_depth : typing.Optional[int]
            Maximum crawl depth

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteIngestionResponse
            Successful Response

        Examples
        --------
        from Infloat import InfloatApi

        client = InfloatApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.crawler.crawl_website(
            url="url",
            chatbot_id="chatbot_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/ingest/website/",
            method="POST",
            json={
                "url": url,
                "chatbot_id": chatbot_id,
                "max_depth": max_depth,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebsiteIngestionResponse,
                    parse_obj_as(
                        type_=WebsiteIngestionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def ingest_youtube(
        self, *, url: str, chatbot_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> YoutubeTranscript:
        """
        Parameters
        ----------
        url : str

        chatbot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        YoutubeTranscript
            Successful Response

        Examples
        --------
        from Infloat import InfloatApi

        client = InfloatApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.crawler.ingest_youtube(
            url="url",
            chatbot_id="chatbot_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/ingest/youtube/",
            method="POST",
            json={
                "url": url,
                "chatbot_id": chatbot_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    YoutubeTranscript,
                    parse_obj_as(
                        type_=YoutubeTranscript,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def upload_document(
        self, *, file: core.File, chatbot_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FilePathResponse:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        chatbot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilePathResponse
            Successful Response

        Examples
        --------
        from Infloat import InfloatApi

        client = InfloatApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.crawler.upload_document(
            chatbot_id="chatbot_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/ingest/document/",
            method="POST",
            data={
                "chatbot_id": chatbot_id,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    FilePathResponse,
                    parse_obj_as(
                        type_=FilePathResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCrawlerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def crawl_website(
        self,
        *,
        url: str,
        chatbot_id: str,
        max_depth: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteIngestionResponse:
        """
        Start a website crawl.

        Parameters
        ----------
        url : str

        chatbot_id : str

        max_depth : typing.Optional[int]
            Maximum crawl depth

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteIngestionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from Infloat import AsyncInfloatApi

        client = AsyncInfloatApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crawler.crawl_website(
                url="url",
                chatbot_id="chatbot_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/ingest/website/",
            method="POST",
            json={
                "url": url,
                "chatbot_id": chatbot_id,
                "max_depth": max_depth,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WebsiteIngestionResponse,
                    parse_obj_as(
                        type_=WebsiteIngestionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def ingest_youtube(
        self, *, url: str, chatbot_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> YoutubeTranscript:
        """
        Parameters
        ----------
        url : str

        chatbot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        YoutubeTranscript
            Successful Response

        Examples
        --------
        import asyncio

        from Infloat import AsyncInfloatApi

        client = AsyncInfloatApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crawler.ingest_youtube(
                url="url",
                chatbot_id="chatbot_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/ingest/youtube/",
            method="POST",
            json={
                "url": url,
                "chatbot_id": chatbot_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    YoutubeTranscript,
                    parse_obj_as(
                        type_=YoutubeTranscript,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def upload_document(
        self, *, file: core.File, chatbot_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> FilePathResponse:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        chatbot_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FilePathResponse
            Successful Response

        Examples
        --------
        import asyncio

        from Infloat import AsyncInfloatApi

        client = AsyncInfloatApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.crawler.upload_document(
                chatbot_id="chatbot_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/ingest/document/",
            method="POST",
            data={
                "chatbot_id": chatbot_id,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    FilePathResponse,
                    parse_obj_as(
                        type_=FilePathResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)