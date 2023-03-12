// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "IWebSocket.h"
#include "Engine/GameInstance.h"
#include "MyProjectCharacter.h"
#include "GameInstance_webSocket.generated.h"
/**
 *
 */
UCLASS()
class MYPROJECT_API UGameInstance_webSocket : public UGameInstance
{
	GENERATED_BODY()
public:
	virtual void Init() override;
	virtual void Shutdown() override;
	TSharedPtr<IWebSocket> WebSocket;
	AMyProjectCharacter* characterpointer;
	 virtual void call_function_for_movement(const FString& message);
	TSharedPtr<IWebSocket> M_WebSocket;

};